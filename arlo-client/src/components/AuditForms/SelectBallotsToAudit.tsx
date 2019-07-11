import React, { useState } from 'react'
import { toast } from 'react-toastify'
import FormSection, { FormSectionDescription } from '../Form/FormSection'
import FormWrapper from '../Form/FormWrapper'
import FormButton from '../Form/FormButton'
import FormButtonBar from '../Form/FormButtonBar'
import { Jurisdiction } from '../../types'
import { api } from '../utilities'

interface Props {
  formOneHasData: any
  formTwoHasData: any
  formThreeHasData: any
  audit: any
  isLoading: any
  deleteBallotManifest: any
  generateOptions: any
  manifestUploaded: any
  setIsLoading: any
  updateAudit: any
  getStatus: any
}

const SelectBallotsToAudit = (props: Props) => {
  const {
    formOneHasData,
    formTwoHasData,
    formThreeHasData,
    audit,
    isLoading,
    deleteBallotManifest,
    generateOptions,
    manifestUploaded,
    setIsLoading,
    updateAudit,
    getStatus,
  } = props

  const [manifestCSV, setManifestCSV] = useState<File | null>()

  const [numAuditBoards, setNumAuditBoards] = useState(
    formTwoHasData && audit.jurisdictions[0].auditBoards.length
  )

  const fileInputChange = (e: any) => {
    const files: any[] = e.target.files
    if (files.length < 1) {
      return
    }
    setManifestCSV(files[0])
  }

  const onAuditBoardsChange = (e: any) => {
    setNumAuditBoards(e.target.value)
  }

  const submitFormTwo = async (e: any) => {
    e.preventDefault()

    const auditBoards = Array.from(Array(numAuditBoards).keys()).map(i => {
      return {
        id: `audit-board-${i + 1}`,
        members: [],
      }
    })

    try {
      // upload jurisdictions
      const data: Jurisdiction[] = [
        {
          id: 'jurisdiction-1',
          name: 'Jurisdiction 1',
          contests: [`contest-1`],
          auditBoards: auditBoards,
        },
      ]
      setIsLoading(true)
      await api('/audit/jurisdictions', {
        method: 'POST',
        body: JSON.stringify({ jurisdictions: data }),
        headers: {
          'Content-Type': 'application/json',
        },
      })

      const newStatus = await getStatus()

      if (newStatus.jurisdictions.length < 1) {
        return
      }
      const jurisdictionID: string = newStatus.jurisdictions[0].id

      // upload form data
      if (!manifestCSV) {
        updateAudit()
        return
      }
      const formData: FormData = new FormData()
      formData.append('manifest', manifestCSV, manifestCSV.name)
      await api(`/jurisdiction/${jurisdictionID}/manifest`, {
        method: 'POST',
        body: formData,
      })

      await updateAudit()
    } catch (err) {
      toast.error(err.message)
    }
    // TODO: Api endpoints not yet clear
  }

  return formOneHasData ? (
    <form onSubmit={submitFormTwo} id="formTwo">
      <FormWrapper>
        {/* <Section>
            <SectionLabel>Estimated Sample Size</SectionLabel>
            <SectionDetail>
                Choose the initial sample size you would like to use for Round 1 of the audit from the options below.
                <div><input name="sampleSize" type="radio" value="223" onChange={e => this.inputChange(e)} /><InputLabel>223 samples (80% chance of reaching risk limit in one round)</InputLabel></div>
                <div><input name="sampleSize" type="radio" value="456" onChange={e => this.inputChange(e)} /><InputLabel>456 samples (90% chance of reaching risk limit in one round)</InputLabel></div>
            </SectionDetail>
        </Section> */}
        <FormSection
          label="Number of Audit Boards"
          description="Set the number of audit boards you with to use."
        >
          <select
            id="auditBoards"
            name="auditBoards"
            value={numAuditBoards}
            onBlur={onAuditBoardsChange}
          >
            {generateOptions(5)}
          </select>
        </FormSection>
        <FormSection label="Ballot Manifest">
          {manifestUploaded ? (
            <React.Fragment>
              <FormSectionDescription>
                <b>Filename:</b>{' '}
                {audit.jurisdictions[0].ballotManifest.filename}
              </FormSectionDescription>
              <FormSectionDescription>
                <b>Ballots:</b>{' '}
                {audit.jurisdictions[0].ballotManifest.numBallots}
              </FormSectionDescription>
              <FormSectionDescription>
                <b>Batches:</b>{' '}
                {audit.jurisdictions[0].ballotManifest.numBatches}
              </FormSectionDescription>
              {!formThreeHasData && (
                <FormButton onClick={deleteBallotManifest}>
                  Delete File
                </FormButton>
              )}
            </React.Fragment>
          ) : (
            <React.Fragment>
              <FormSectionDescription>
                Click &quot;Browse&quot; to choose the appropriate Ballot
                Manifest file from your computer
              </FormSectionDescription>
              <input
                type="file"
                accept=".csv"
                onChange={fileInputChange}
              ></input>
            </React.Fragment>
          )}
        </FormSection>
      </FormWrapper>
      {!formThreeHasData && isLoading && <p>Loading...</p>}
      {!formThreeHasData && !isLoading && (
        <FormButtonBar>
          <FormButton onClick={submitFormTwo}>
            Select Ballots To Audit
          </FormButton>
        </FormButtonBar>
      )}
    </form>
  ) : (
    <div></div>
  )
}

export default React.memo(SelectBallotsToAudit)
